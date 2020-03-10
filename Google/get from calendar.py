#!/usr/bin/env python

import sys

from oauth2client import client
from googleapiclient import sample_tools



def getAttendies(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'calendar', 'v3', __doc__, __file__,
        scope='https://www.googleapis.com/auth/calendar.readonly')

    calendarlist = service.calendarList().list().execute()
    calendar_id = calendarlist['items'][0]['id']
    query = "Jedi"
    events = service.events().list(calendarId=calendar_id, q=query, singleEvents='True', orderBy='startTime').execute()
    events = events.get('items', [])

    try:
        i = 1
        for event in events:
            start = event['start'].get('dateTime')
            print(i, event['summary'])
            print(start)
            for attendees in event['attendees']:
                atte = attendees.get('displayName', 'email')
                print(" ( " + attendees['email'] + ")")
            i += 1
            print('_____________________________________')
        i = 1

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize.')

def main(argv):

    getAttendies(argv)

if __name__ == "__main__":
    main(sys.argv)