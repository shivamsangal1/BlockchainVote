import sqlite3

class generateResults:

    def genResult(self,election_id):
        conn = sqlite3.connect("ivote.db")
        c = conn.cursor()
        c.execute("select ended from election where electionid="+str(election_id))
        r = c.fetchall()
        if(r[0]=='F') :
            c.execute("update election set ended='T' where electionid="+str(election_id))
            c.execute("select vote_given, count(*) from election"+str(election_id)+" group by vote_given")
            
            r = c.fetchall()
            for i in r:
                c.execute("insert into result('"+str(election_id)+",'"+str(r[0])+"'"+str(r[1])+")")
            return "result generated"
        else :
            return "result already generated"
