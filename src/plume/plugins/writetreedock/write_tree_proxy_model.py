'''
Created on 26 may 2015

@author:  Cyril Jacquet
'''

from PyQt5.QtCore import QSortFilterProxyModel, QVariant, QModelIndex, Qt


class WriteTreeProxyModel(QSortFilterProxyModel):

    '''
    WriteTreeProxyModel
    '''

    def __init__(self, parent=None):
        '''
        Constructor
        '''

        super(WriteTreeProxyModel, self).__init__(parent=None)

    def node_from_index(self, index):
        return self.sourceModel().node_from_index(self.mapToSource(index))

    @property
    def id_of_last_created_sheet(self):
        return self.sourceModel().id_of_last_created_sheet

    def find_index_from_id(self, id_):
        index = self.sourceModel().find_index_from_id(id_)
        print(index.isValid())
        return self.mapFromSource(index)

    def insert_child_row(self, parent_index):
        return self.sourceModel().insert_child_row(self.mapToSource(parent_index))

    def insert_row_after(self, parent_index):
        return self.sourceModel().insert_row_by(self.mapToSource(parent_index))

    def filterAcceptsRow(self, p_int, index):
        if index.data(self.sourceModel().DeletedRole) == 1:
            return False
        else:
            return QSortFilterProxyModel.filterAcceptsRow(self, p_int, index)
