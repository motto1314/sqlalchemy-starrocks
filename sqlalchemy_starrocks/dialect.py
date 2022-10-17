# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.dialects.mysql.mysqldb import MySQLDialect_mysqldb

class SRDialect(MySQLDialect_mysqldb):

    name = 'sr'

    def __init__(self, *args, **kw):
        super(SRDialect, self).__init__(*args, **kw)
        self.ischema_names = self.ischema_names.copy()
        self.ischema_names['largeint']=BIGINT

    @classmethod
    def dbapi(cls):
        return __import__("MySQLdb")
