#!/usr/bin/env python3
import argparse

from sweepai.logic import process_issue_text


def main():
    parser = argparse.ArgumentParser(description="Process issue text and output Sweep's execution plan.")
    parser.add_argument("issue_text", type=str, help="The text of the issue to process.")
    
    args = parser.parse_args()
    issue_text = args.issue_text
    
    files_to_change, execution_plan = process_issue_text(issue_text)
    
    print("Files to be changed:")
    for file in files_to_change:
        print(f"- {file}")
    
    print("\nProposed Execution Plan:")
    print(execution_plan)

if __name__ == "__main__":
    main()
