

class Label:
    def __init__(self, fName):
        self.kvTable = {}
        self.groups = {}
        self.objects = {}

        with open(fName, 'r') as f:


            while True:


                if self.peek_line(f) is None or \
                        self.peek_line(f).strip() == 'END':
                    break

                if len(self.peek_line(f)) > 0 and self.peek_line(f).find('/*') < 0:

                    if self.peek_line(f).find("OBJECT") == 0:

                        self.parse_obj(f)
                    elif self.peek_line(f).find("GROUP") == 0:

                        self.parse_group(f)
                    else:

                        self.parse_kv_table(f)
                else:
                    f.readline()

        # print('kvs: {}'.format(self.kvTable))
        # print('groups: {}'.format(self.groups))
        print('objects: {}'.format(self.objects))


    # parse helper functions

    def peek_line(self, f):
        pos = f.tell()
        line = f.readline()
        f.seek(pos)
        return line

    def split_kv(self, line):

        kv = line.split('=')

        if len(kv) != 2:
            # print("invalid kv pair: {}".format(line))
            return None

        key = kv[0].strip()
        value = kv[1].strip()

        return (key, value)

    def parse_kv(self, f):

        line = f.readline()
        ret = self.split_kv(line)

        if ret is None:
            return None

        (key, value) = ret

        while True:

            if self.peek_line(f) is None or \
                    self.peek_line(f).find('=') >= 0 or \
                    self.peek_line(f).find('END') >= 0:
                break

            # this is a multi-line value
            line = f.readline()
            value += line.strip()

        return (key, value)

    def parse_kv_table(self, f):

        ret = self.parse_kv(f)

        if ret is None:
            return None

        (key, value) = ret

        # print('Parsing entry "{} : {}"'.format(key, value))
        self.kvTable[key] = value

    def parse_obj(self, f):

        line = f.readline()
        (objKey, objName) = self.split_kv(line)
        value_dict = {}

        print("parsing object: {}".format(objName))

        while True:

            line = self.peek_line(f)
            if line is None:
                print("got empty line in object")
                return
            elif line.find("END_OBJECT") >= 0:
                print("reached end of object")
                break

            ret = self.parse_kv(f)

            if ret is None:
                print("empty kv pair")
                break

            (k, v) = ret
            value_dict[k] = v

        self.objects[objName] = value_dict

    def parse_group(self, f):

        line = f.readline()
        (grpKey, grpName) = self.split_kv(line)
        value_dict = {}

        while True:

            line = self.peek_line(f)
            if line is None:
                return
            elif line.find("END_GROUP") >= 0:
                break

            ret = self.parse_kv(f)

            if ret is None:
                break

            (k, v) = ret
            value_dict[k] = v

        self.groups[grpName] = value_dict
