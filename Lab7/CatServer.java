import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileNotFoundException;

/**
 * CatServer is the RMI server that implements the CatFileInterface.
 * It allows clients to remotely read a file line by line.
 */
public class CatServer extends UnicastRemoteObject implements CatFileInterface {

    // Member variable to hold the state (the open file)
    private BufferedReader fileReader;

    // Constructor
    protected CatServer() throws RemoteException {
        super(); // Call constructor of UnicastRemoteObject
        fileReader = null; // No file is open initially
    }

    @Override
    public synchronized boolean openFile(String filename) throws RemoteException {
        // If a file is already open, close it first.
        if (fileReader != null) {
            closeFile();
        }

        try {
            // Try to open the new file
            FileReader fr = new FileReader(filename);
            fileReader = new BufferedReader(fr);
            System.out.println("[Server] Opened file: " + filename);
            return true;
        } catch (FileNotFoundException e) {
            System.err.println("[Server] Error: File not found: " + filename);
            fileReader = null;
            return false;
        }
    }

    @Override
    public synchronized String nextLine() throws RemoteException {
        // Check if a file is open
        if (fileReader == null) {
            System.err.println("[Server] Client tried to read, but no file is open.");
            return null;
        }

        try {
            // Read the next line
            String line = fileReader.readLine();
            
            // readLine() returns null at end-of-file
            if (line == null) {
                System.out.println("[Server] Reached end-of-file.");
            }
            
            return line;
        } catch (IOException e) {
            System.err.println("[Server] Error reading from file: " + e.getMessage());
            return null;
        }
    }

    @Override
    public synchronized boolean closeFile() throws RemoteException {
        // Check if a file is even open
        if (fileReader == null) {
            return true; // Already "closed"
        }

        try {
            fileReader.close();
            fileReader = null; // Reset the state
            System.out.println("[Server] File closed.");
            return true;
        } catch (IOException e) {
            System.err.println("[Server] Error closing file: " + e.getMessage());
            return false;
        }
    }

    // Main method to start the server and RMI registry
    public static void main(String[] args) {
        try {
            // 1. Create and start the RMI registry on the default port 1099
            LocateRegistry.createRegistry(1099);
            System.out.println("RMI registry created.");

            // 2. Create the server object
            CatServer server = new CatServer();
            System.out.println("CatServer object created.");

            // 3. Bind the server object to a name in the registry
            String serverName = "CatFileServer";
            Naming.rebind(serverName, server);
            
            System.out.println("CatServer is ready and bound as '" + serverName + "'.");
            System.out.println("Waiting for client connections...");

        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}