#!/bin/bash
# Script to run all Python scripts and create figures
python3 plot_opinion_length.py
python3 plot_opinion_count.py
python3 count_of_decisions_by_year.py
python3 count_of_decisions_by_chief.py
python3 count_of_decisions_by_pres_term.py
python3 time_to_decision_by_year.py
python3 time_to_decision_by_chief.py
python3 time_to_decision_by_pres_term.py
echo "All figures created."