#!/usr/bin/env python

# TODO: check dest of teams drive change q for regular

def checkDest(API, file, folder_id):
    """
    checks a folder for FILE
    RETURNS: true if it finds FILE in storage
            false if its not there
    """
    page_token = None
    response = API.files().list(q=f"'{folder_id}' in parents", supportsTeamDrives=True,includeTeamDriveItems=True, spaces='drive',
                                fields='nextPageToken, files(id, name)',
                                pageToken=page_token).execute()
    items = response.get('files', [])
    #print(items)
    for i in range(0, len(items)):
        r = items[i].get('name').split('.', 2)
        w = file.split('.', 2)

        if w[1] == r[1] and w[2] == r[2] and i <= len(items):
            return True
    return False


def main():
    API = 'API'
    file = 'file'
    folder = 'folder id'

    checkDest(API,file,folder)

if __name__ == "__main__":
    main()
