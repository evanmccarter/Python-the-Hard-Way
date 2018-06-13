import ex40_My_Stuff

# module style
ex40_My_Stuff.apple()
print ex40_My_Stuff.tangerine


class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    
    def apple(self):
        print "APPPPPPPLES"


# class style
thing = MyStuff()
thing.apple()
print thing.tangerine
