class ClassObj:
    _dogs = [{'id': 1, 'name': 'chichi'}]

    def getDogs(self):
        return self._dogs


classObj = ClassObj()

dogs = classObj.getDogs()

print('dogs ', dogs[0]['id'])
