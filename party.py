# This file is part party_tradename module for Tryton.  The COPYRIGHT file at
# the top level of this repository contains the full copyright notices and
# license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond import backend


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'
    trade_name = fields.Char('Trade Name')

    @classmethod
    def __register__(cls, module_name):
        super(Party, cls).__register__(module_name)
        table = backend.TableHandler(cls, module_name)
        table.column_rename('tradename', 'trade_name')

    @classmethod
    def search_rec_name(cls, name, clause):
        domain = super(Party, cls).search_rec_name(name, clause)
        if clause[1].startswith('!') or clause[1].startswith('not '):
            bool_op = 'AND'
        else:
            bool_op = 'OR'
        return [bool_op,
            domain,
            ('trade_name',) + tuple(clause[1:]),
            ]
