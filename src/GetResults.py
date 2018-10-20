from CreateHits import get_balance
import xmltodict
import pprint

def get_answers(worker_results, hit_id):
    print(hit_id)
    if worker_results['NumResults'] > 0:
        for assignment in worker_results['Assignments']:
            xml_doc = xmltodict.parse(assignment['Answer'])
            
            print("Worker's answer was:")
            if type(xml_doc['QuestionFormAnswers']['Answer']) is list:
                # Multiple fields in HIT layout
                for answer_field in xml_doc['QuestionFormAnswers']['Answer']:
                    print("For input field: " + answer_field['QuestionIdentifier'])
                    print("Submitted answer: " + answer_field['FreeText'])
            else:
                # One field found in HIT layout
                print("For input field: " + xml_doc['QuestionFormAnswers']['Answer']['QuestionIdentifier'])
                print("Submitted answer: " + xml_doc['QuestionFormAnswers']['Answer']['FreeText'])
    else:
        print("No results ready yet")

def get_results(mturk, hits):
    results = []
    hit_id = hits[0]
    for hit_id in hits:
        worker_results = mturk.list_assignments_for_hit(HITId=hit_id, AssignmentStatuses=['Submitted'])
        get_answers(worker_results, hit_id)
        results.append(worker_results)
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(results)
    
    return results

def main():
    mturk = get_balance()
    hits = []
    with open('hits/last_hits.csv', 'r') as input:
        next(input)
        for hit in input:
            hits.append(hit.strip('\n'))
    # print(hits)
    results = get_results(mturk, hits)

if __name__ == '__main__':
    main()