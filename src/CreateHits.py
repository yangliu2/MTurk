import boto3
MTURK_SANDBOX = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
MTURK = 'https://mturk-requester.us-east-1.amazonaws.com'

def get_balance(profile_name='mturk', endpoint='sandbox'):
    # switch between sandbox and prod
    if endpoint == 'sandbox':
        endpoint_url = MTURK_SANDBOX
    elif endpoint == 'prod':
        endpoint_url = MTURK

    # profile name from ~/.aws/credentials file
    session = boto3.Session(profile_name=profile_name)
    client = session.client(
        'mturk', 
        region_name='us-east-1',
        endpoint_url = endpoint_url)

    print("I have $" + client.get_account_balance()['AvailableBalance'] + " in my Sandbox account")
    return client

def create_hit(mturk):
    question = open('templates/questions.xml', 'r').read()
    new_hit = mturk.create_hit(
        Title = 'Is this Tweet happy, angry, excited, scared, annoyed or upset?',
        Description = 'Read this tweet and type out one word to describe the emotion of the person posting it: happy, angry, scared, annoyed or upset',
        Keywords = 'text, quick, labeling',
        Reward = '0.2',
        MaxAssignments = 1,
        LifetimeInSeconds = 60 * 60 * 48, # lenght on market
        AssignmentDurationInSeconds = 60 * 10, # time to complete once opened
        AutoApprovalDelayInSeconds = 60 * 60 * 4, # time until automatic approval if no user did it
        Question = question,
    )
    print("A new HIT has been created. You can preview it here:")
    print("https://workersandbox.mturk.com/mturk/preview?groupId=" + new_hit['HIT']['HITGroupId'])
    print("HITID = " + new_hit['HIT']['HITId'] + " (Use to Get Results)")
    # Remember to modify the URL above when you're publishing
    # HITs to the live marketplace.
    # Use: https://worker.mturk.com/mturk/preview?groupId=

def main():
    mturk = get_balance('tic')
    # create_hit(mturk)
    


if __name__ == '__main__':
    main()