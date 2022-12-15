#!/usr/bin/env python3

# The Notices and Disclaimers for Ocean Worlds Autonomy Testbed for Exploration
# Research and Simulation can be found in README.md in the root directory of
# this repository.

from ow_lander.actions import lander
from ow_lander import node_helper

import argparse

parser = argparse.ArgumentParser(
  formatter_class=argparse.ArgumentDefaultsHelpFormatter,
  description="Ingest material present in the sample dock."
)
args = parser.parse_args()

node_helper.call_single_use_action_client(lander.DockIngestSampleServer,
  **vars(args))
