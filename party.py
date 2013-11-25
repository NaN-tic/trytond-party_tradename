#This file is part party_tradename module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.transaction import Transaction
from trytond import backend

__all__ = ['Party']
__metaclass__ = PoolMeta


class Party:
    __name__ = 'party.party'
    trade_name = fields.Char('Trade Name')

    @classmethod
    def __register__(cls, module_name):
        cursor = Transaction().cursor
        TableHandler = backend.get('TableHandler')
        super(Party, cls).__register__(module_name)
        table = TableHandler(cursor, cls, module_name)
        table.column_rename('tradename', 'trade_name')

    @classmethod
    def search_rec_name(cls, name, clause):
        res = super(Party, cls).search_rec_name(name, clause)
        return ['OR', [res], [('trade_name',) + tuple(clause[1:])]]
