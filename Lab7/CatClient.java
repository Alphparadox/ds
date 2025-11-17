import java.rmi.Naming;
import java.rmi.RemoteException;

/**
 * CatClient connects to the CatServer and requests to read a file line-by-line.
 */
public class CatClient {

    public static void main(String[] args) {
        // The file we want to read from the server
        String filenameToRead = "sample.txt";
        String serverHost = "localhost";
        String serverName = "CatFileServer";

        try {
            // 1. Look up the remote object from the RMI registry
            String lookupURL = "rmi://" + serverHost + "/" + serverName;
            CatFileInterface server = (CatFileInterface) Naming.lookup(lookupURL);
            System.out.println("Connected to server at: " + lookupURL);

            // 2. Request to open the file
            System.out.println("Requesting to open file: " + filenameToRead);
            if (server.openFile(filenameToRead)) {
                System.out.println("File opened successfully. Reading contents:");
                System.out.println("-------------------------------------------");

                // 3. Read the file line-by-line
                String line;
                while ((line = server.nextLine()) != null) {
                    System.out.println(line);
                }
                
                System.out.println("-------------------------------------------");
                System.out.println("--- End of File ---");

                // 4. Close the file
                if (server.closeFile()) {
                    System.out.println("File closed on server.");
                } else {
                    System.out.println("Error closing file on server.");
                }

            } else {
                // If openFile failed
                System.err.println("Server failed to open the file: " + filenameToRead);
            }

        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}