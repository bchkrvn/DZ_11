import json

from class_candidat import Candidate

CANDIDATES_FILE_NAME = 'candidates.json'


def load_candidates() -> dict:
    with open(CANDIDATES_FILE_NAME, encoding='utf-8') as file:
        candidates_load = json.load(file)
        candidates = {str(candidate['id']): Candidate(*candidate.values()) for candidate in candidates_load}

    return candidates


def get_candidates_by_name(candidate_name: str, candidates: dict) -> list:
    needed_candidates = [candidate for candidate in candidates.values() if
                         candidate_name.capitalize() in candidate.get_name().split()]
    return needed_candidates


def get_candidates_by_skill(skill_name: str, candidates: dict) -> list:
    needed_candidates = [candidate for candidate in candidates.values() if skill_name.lower() in candidate.get_skills()]
    return needed_candidates
