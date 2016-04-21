# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import logging
import time

from data_pipeline.tools.meteorite_wrappers import StatTimer
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from yelp_lib.containers.lists import unlist

from replication_handler import config
from replication_handler.models.database import Base
from replication_handler.models.database import default_now
from replication_handler.models.database import UnixTimeStampType


log = logging.getLogger('replication_handler.models.data_event_checkpoint')


DATA_EVENT_CHECKPOINT_TIMER_NAME = 'replication_handler_data_event_checkpoint_timer'


class DataEventCheckpoint(Base):

    __tablename__ = 'data_event_checkpoint'

    id = Column(Integer, primary_key=True)
    kafka_topic = Column(String, nullable=False)
    kafka_offset = Column(Integer, nullable=False)
    cluster_name = Column(String, nullable=False)
    time_created = Column(UnixTimeStampType, default=default_now)
    time_updated = Column(UnixTimeStampType, default=default_now, onupdate=default_now)

    @classmethod
    def upsert_data_event_checkpoint(
        cls,
        session,
        topic_to_kafka_offset_map,
        cluster_name,
    ):
        timer = StatTimer(
            DATA_EVENT_CHECKPOINT_TIMER_NAME,
            container_name=config.env_config.container_name,
            container_env=config.env_config.container_env,
            rbr_source_cluster=config.env_config.rbr_source_cluster,
        )
        timer.start()
        for topic, offset in topic_to_kafka_offset_map.iteritems():
            data_event_checkpoint = session.query(
                DataEventCheckpoint
            ).filter(
                DataEventCheckpoint.kafka_topic == topic,
                DataEventCheckpoint.cluster_name == cluster_name
            ).all()
            data_event_checkpoint = unlist(data_event_checkpoint)
            if data_event_checkpoint is None:
                data_event_checkpoint = DataEventCheckpoint()
            data_event_checkpoint.kafka_topic = topic
            data_event_checkpoint.kafka_offset = offset
            data_event_checkpoint.cluster_name = cluster_name
            # Log data with current time (not necessarily
            # the time on the event time field)
            log.info(
                'Reached checkpoint with offset {} on topic {} at time {}.'.
                format(offset, topic, int(time.time()))
            )
            session.add(data_event_checkpoint)
        timer.stop()

    @classmethod
    def get_topic_to_kafka_offset_map(cls, session, cluster_name):
        topic_to_kafka_offset_map = {}
        records = session.query(
            DataEventCheckpoint
        ).filter(
            DataEventCheckpoint.cluster_name == cluster_name
        ).all()
        for record in records:
            topic_to_kafka_offset_map[record.kafka_topic] = record.kafka_offset
        return topic_to_kafka_offset_map
