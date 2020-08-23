# from airtable get next name + source that is not muted. 
# Take earliest date and if tied take random from remaining. 
from airtable import Airtable
from keys import airtable_api_key, airtable_base_key
from datetime import datetime



airtable_obj = Airtable(base_key=airtable_base_key, table_name='contacts', api_key=airtable_api_key)


def get_friend():
    for page in airtable_obj.get_iter(max_records=1, view='priority_queue'):
        for record in page:
            user_records = record
            
    user_id = user_records['id']
    friend_id = user_id
    friend_name = user_records['fields']['name']
    friend_source = user_records['fields']['source']
        
    return friend_id, friend_name, friend_source

def update_considering(friend_id, indicator):
    update_dict = {'in_consideration': indicator}
    airtable_obj.update(friend_id, update_dict)
    print('marked as considering')
    

def get_considered():
    for page in airtable_obj.get_iter(max_records=1, view='in_consideration'):
        for record in page:
            user_records = record
            
    user_id = user_records['id']
    friend_id = user_id
    friend_name = user_records['fields']['name']
    friend_source = user_records['fields']['source']

    return friend_id, friend_name, friend_source


def mark_as_skipped(friend_id):
    update_dict = {'last_skipped': datetime.today().strftime('%Y-%m-%d')}
    airtable_obj.update(friend_id, update_dict)
    print('marked as skip')


def mute_person(friend_id):
    update_dict = {'muted': True}    
    airtable_obj.update(friend_id, update_dict)
    print('muted')    


# did you talk to this person 
#   - get some response and input that as True for False
def mark_as_talked(friend_id, follow_up_val):
    update_dict = {'follow_up': follow_up_val}
    if follow_up_val:
        update_dict = {'follow_up': follow_up_val,
                'last_contact': datetime.today().strftime('%Y-%m-%d')}
    airtable_obj.update(friend_id, update_dict)
    print('marked date of convo')

  
# user flow: 

# at 6pm:
# do you want to talk to __ today?  -- get_friend()
    # yes
        # follow up text 2 hours later at 8pm -- did you talk to __ today? 
            # yes
                # update user with current date for last talked
            # no
                # do nothing 
    # no
        # mark skip date as today
        # query next user 
    # mute
        # update user as muted
        # query next user 
    
    
    
