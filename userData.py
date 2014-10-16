__author__ = 'midhun7416'

import time
from random import randint

BIG_L = 65
BIG_H = 90
LOW_H = 97
LOW_L = 122
USER_NAME_MAX = 16
MAX_USERS = 300;
DOCS_MAX = 2100;
VERSION_HISTORY = 2100
PERMISSION_MAX = 2100
FOLDER_MAX = 300

class Users:
    def __init__(self, userid, user_name, password, home_dir):
        self.user_id = userid
        self.user_name = user_name
        self.password = password
        self.home_dir = home_dir

class Doc:
    TYPES = ['jpg', 'pdf', 'docx', 'ppt', 'txt']
    def __init__(self, doc_id, doc_name, doc_type,doc_size,creation_date,
                 modified_date,modified_by,owner,version,parent_doc_id,folder_id):
        self.doc_id = doc_id
        self.doc_name = doc_name
        self.doc_type = doc_type
        self.doc_size = doc_size
        self.creation_date = creation_date
        self.modified_date = modified_date
        self.modified_by = modified_by
        self.owner = owner
        self.version = version
        self.parent_doc_id = parent_doc_id
        self.folder_id = folder_id

class VersionHistory:
    def __init__(self, doc_id, modified_date, modified_by, version):
        self.doc_id = doc_id
        self.modified_date = modified_date
        self.modified_by = modified_by
        self.version = version

class Permission:
    VALUES = ['r', 'w', 'x', 'rwx']
    def __init__(self, doc_id, user_id, permission_name):
        self.doc_id = doc_id
        self.user_id = user_id
        self.permission_name = permission_name

class Folder:
    def __init__(self, folder_id, folder_name, user_id):
        self.folder_id = folder_id
        self.folder_name = folder_name
        self.user_id = user_id


class DataGenerator:
    globals()
    userID = 1
    docID = 1
    folderID = 1
    userList = []
    docList = []
    versionList = []
    permissionList = []
    folderList = []
    def __init__(self):
        pass

    def getRandom(self, left, right):
        return randint(left,right)


    def generateString(self, length):
        str = ''
        for i in range(1,length):
            str += chr(self.getRandom(BIG_L,BIG_H))
        return str


    def generateUser(self):
        userNameLen = self.getRandom(2,USER_NAME_MAX)
        user_name = self.generateString(userNameLen)
        password = self.generateString(16)
        newUser = Users(self.userID, user_name, password, '/home/'+user_name)
        self.userList.append(newUser)
        self.userID += 1
        return newUser


    def generateDoc(self,user_name, folder_id):
        doc_name = user_name + str(self.docID)
        doc_type = Doc.TYPES[self.getRandom(0, len(Doc.TYPES)-1)]
        doc_size = self.getRandom(1, 10000)
        creation_date = time.asctime()
        modified_date = time.asctime()
        doc = Doc(self.docID,doc_name, doc_type, doc_size, creation_date, modified_date,
                    user_name, user_name, 1, 0, folder_id)
        self.docList.append(doc)
        self.docID += 1
        return doc

    def generateVersionHistory(self, doc_id, modified_date, modified_by, version):
        versionObj = VersionHistory(doc_id, modified_date, modified_by, version)
        self.versionList.append(versionObj)
        return versionObj


    def generatePermission(self, doc_id, user_id):
        permission = Permission(doc_id, user_id, 'rwx')
        self.permissionList.append(permission)
        return permission


    def generateFolder(self, folder_name, user_id):
        folder = Folder(self.folderID, folder_name, user_id)
        self.folderList.append(folder)
        self.folderID += 1
        return folder


    def modifyDocs(self):
        pass


    def addPermissions(self):
        import random
        self.permissionList = random.shuffle(self.permissionList)
        for p in range(0, len(self.permissionList)/2):
            if MAX_USERS - p.user_id > 13 :
                for u in range(0, 10):
                    permVal = Permission.VALUES[self.getRandom(0, len(Permission.VALUES)-1)]
                    user_id = self.getRandom(p.user_id+1, MAX_USERS)
                    perm = Permission(p.doc_id, user_id, permVal)
                    self.permissionList.append(perm)



    def generateData(self):
        for userCount in range(1,MAX_USERS):
            user = self.generateUser()
            folder = self.generateFolder(user.home_dir, user.user_id)
            for docCount in range(1, DOCS_MAX/MAX_USERS):
                doc = self.generateDoc(user.user_name, folder.folder_id)
                perm = self.generatePermission(doc.doc_id, user.user_id)
                version = self.generateVersionHistory(doc.doc_id, doc.modified_date,
                                                      doc.modified_by,doc.version)
        self.addPermissions()
        self.modifyDocs()

    def writeData(self):
        ufile = open('users', 'w')
        dfile = open('docs', 'w')
        ffile = open('folder', 'w')
        pfile = open('perm', 'w')
        vfile = open('version', 'w')
        for u in self.userList:
            ufile.write(str(u.user_id))
            ufile.write(u.user_name)
            ufile.write(u.password)
            ufile.write(u.home_dir)
        for d in self.docList:
            dfile.write(str(d.doc_id))
        for p in self.permissionList:
            pfile.write()
        for v in self.versionList:
            vfile.write()
        for f in self.folderList:
            ffile.write(str(u.folder_id))
            ffile.write('\t'+str(u.folder_name))
            ffile.write('\t'+str(u.user_id)+'\n')




if __name__ == '__main__':
    data = DataGenerator()
    data.generateData()
    data.writeData()


