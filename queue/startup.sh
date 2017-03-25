#!/bin/bash

( sleep 5
rabbitmqctl add_user scoring_engine scoring_engine 2> /dev/null
rabbitmqctl set_permissions scoring_engine '.*' '.*' '.*' 2> /dev/null ) &

rabbitmq-server $@
