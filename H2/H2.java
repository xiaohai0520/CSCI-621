import java.sql.*;
public class H2 {
    private Connection conn;
    private Statement stmt;

    public H2() throws SQLException{
        //connect to the database
        conn = DriverManager.getConnection("jdbc:h2:~/test", "sa", "");
        //init a statement
        stmt=conn.createStatement();
    }

    public static void main(String[] a) throws Exception {
        // create a new h2 instance
        H2 h2 = new H2();

        // clear table
        h2.stmt.executeUpdate("DROP table students IF EXISTS ");

        //create a table
        String sqlCreateTable = "CREATE TABLE students(id INT,name VARCHAR(255));" ;
        h2.stmt.execute(sqlCreateTable);

        //insert data
        String sqlInsert = "INSERT INTO students VALUES(1,'Peter')";
        h2.stmt.execute(sqlInsert);
        sqlInsert = "INSERT INTO students VALUES(2,'Mary')";
        h2.stmt.execute(sqlInsert);

        //read data
        String sqlRead = "SELECT * FROM students";
        ResultSet rset=h2.stmt.executeQuery(sqlRead);
        while(rset.next()){
            System.out.println(rset.getInt("id")+"  "+rset.getString("name"));
        }

        //update
        String sqlUpdate = "update students set name = 'Kate' where id = 1";
        h2.stmt.execute(sqlUpdate);

        //delete
        String sqlDelete = "delete from students where id = 2";
        h2.stmt.execute(sqlDelete);
        rset=h2.stmt.executeQuery(sqlRead);
        while(rset.next()){
            System.out.println(rset.getInt("id")+"  "+rset.getString("name"));
        }


        // close
        rset.close();
        h2.stmt.close();
        h2.conn.close();
    }
}
