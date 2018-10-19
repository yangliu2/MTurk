from CreateHits import get_balance
import xmltodict
import pprint

def get_results(mturk, hits):
    results = []
    for hit_id in hits:
        worker_results = mturk.list_assignments_for_hit(HITId=hit_id, AssignmentStatuses=['Submitted'])
        results.append(worker_results)
    print(len(results))
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(results)
    return results

def main():
    mturk = get_balance()
    hits = ['3W9XHF7WGLJJRDHRMPAGCPD8UJSTKB', '39HYCOOPKP970CLXLBNHMYNQG2ZMDQ']
    results = get_results(mturk, hits)

if __name__ == '__main__':
    main()