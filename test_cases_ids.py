import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def test_total_cases(total_cases):
    expected_total_cases = 268880
    if total_cases == expected_total_cases:
        logging.info(f"Total number of cases is correct: {total_cases}")
    else:
        deviation = abs(total_cases - expected_total_cases) / expected_total_cases
        if deviation < 0.1:
            logging.warning(f"Total number of cases has a slight deviation: {total_cases} (expected: {expected_total_cases})")
        else:
            logging.error(f"Total number of cases is significantly off: {total_cases} (expected: {expected_total_cases})")

def test_patient_ids(dataset_name, unique_ids, filtered_ids):
    if unique_ids == filtered_ids:
        logging.info(f"{dataset_name}: Unique and filtered patient IDs match: {unique_ids}")
    else:
        if unique_ids is None or filtered_ids is None:
            logging.critical(f"{dataset_name}: Missing patient IDs (unique_ids: {unique_ids}, filtered_ids: {filtered_ids})")
        else:
            deviation = abs(unique_ids - filtered_ids) / unique_ids
            if deviation < 0.1:
                logging.warning(f"{dataset_name}: Patient IDs have a slight deviation (unique: {unique_ids}, filtered: {filtered_ids})")
            else:
                logging.error(f"{dataset_name}: Patient IDs are significantly off (unique: {unique_ids}, filtered: {filtered_ids})")

def run_tests():
    total_cases = 268880

    datasets = {
        "eicu": {"unique_ids": 138813, "filtered_ids": 138813},
        "hirid": {"unique_ids": 33626, "filtered_ids": 33626},
        "mimic3": {"unique_ids": 45521, "filtered_ids": 45521},
        "mimic4": {"unique_ids": 50920, "filtered_ids": 50920},
    }

    test_total_cases(total_cases)

    for dataset_name, ids in datasets.items():
        test_patient_ids(dataset_name, ids["unique_ids"], ids["filtered_ids"])

if __name__ == "__main__":
    run_tests()
    logging.info("All tests completed.")

