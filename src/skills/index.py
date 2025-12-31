import pandas as pd

# --------------------------------------------------
# Build an inverted index: skill -> list of job_ids
# --------------------------------------------------
def build_inverted_index(df, job_id_col="job_id", skills_col="skills"):
    # Local dictionary that will store the index
    # Example:
    # {
    #   "python": [1, 3, 10],
    #   "sql": [1, 2]
    # }
    index = {}

    # Loop over each job_id and its associated skills list
    for job_id, skills in zip(df[job_id_col], df[skills_col]):

        # If a job has no skills (empty list or None), skip it
        if not skills:
            continue

        # For each skill in the job's skill list
        for skill in skills:
            # If this skill is not yet in the index, create an empty list
            if skill not in index:
                index[skill] = []

            # Add the job_id to the list of jobs for this skill
            index[skill].append(job_id)

    # Remove duplicates and sort job_ids for each skill
    # (a job should not appear twice for the same skill)
    for skill in index:
        index[skill] = sorted(set(index[skill]))

    # Return the completed inverted index
    return index


# --------------------------------------------------
# Search helper: return all job_ids for a given skill
# --------------------------------------------------
def search(index, skill):
    # If the skill exists in the index, return its job_ids
    # Otherwise, return an empty list
    return index.get(skill, [])





