import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 * CatFileInterface defines the remote methods that the CatServer will implement.
 */
public interface CatFileInterface extends Remote {

    /**
     * Opens a file on the server.
     * @param filename The name of the file to open.
     * @return true if the file was opened successfully, false otherwise.
     */
    public boolean openFile(String filename) throws RemoteException;

    /**
     * Reads the next line from the currently open file.
     * @return The next line as a String, or null if EOF is reached or no file is open.
     */
    public String nextLine() throws RemoteException;

    /**
     * Closes the currently open file.
     * @return true if the file was closed successfully, false otherwise.
     */
    public boolean closeFile() throws RemoteException;
}