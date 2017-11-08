#!/usr/bin/env bash
. $HOME/af_env.sh
py3clean .
export AF_TEST_SUITE_NAME='Seed PAQX Parent'
python $AF_RUN_JOBS_PATH/run_seed_paqx_parent_test_suite.py
export AF_TEST_SUITE_NAME='Test Suite Name Not Set'