#coding: utf-8

import os
import sys

class Main(object):
    def __init__(self):
        self.where = []

    # newLine 或是提取的時候
    def __repr__(self):
        self.execute()
        # make self as a List Object instead of super(Main, self).__repr__()
        return repr(' and '.join(self.where))

    # 掉用 len() 時候提取
    def __len__(self):
        self.execute()
        return len(self.where)

    # for-loop 調用
    def __iter__(self):
        self.execute()
        return iter(self.where)

    # get 單獨一筆的時候 obj[index], SQL: LIMIT 1 OFFSET idx
    def __getitem__(self, idx):
        self.execute(idx)
        return self.where[idx]

    # 真正的執行 Method
    def execute(self, idx=None):
        sql = 'get object for repress'
        if idx is not None:
            sql += ' with args: %s' % (repr(idx))
        print sql

    # 實作串接 API
    def query(self, args):
        # keep per condition unique
        self.where.append(str(args))
        self.where = list(set(self.where))
        return self

if __name__ == '__main__':
    app = Main()
    cache = app.query('id >= 1').query('name != null').query('status = 1')      # execute __repr__ not yet
    print cache      # execute __repr__
    import pdb; pdb.set_trace()
