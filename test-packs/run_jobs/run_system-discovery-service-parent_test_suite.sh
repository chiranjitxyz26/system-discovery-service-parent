#!/usr/bin/env bash
. $HOME/af_env.sh
py3clean .
export AF_TEST_SUITE_NAME='System Discovery Service Parent'
python $AF_RUN_JOBS_PATH/run_system-discovery-service-parent_test_suite.py
export AF_TEST_SUITE_NAME='Test Suite Name Not Set'