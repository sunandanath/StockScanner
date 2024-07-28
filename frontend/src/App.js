import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [csvUrl, setCsvUrl] = useState("");
  const [htmlUrl, setHtmlUrl] = useState("");
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleFileUpload = () => {
    const formData = new FormData();
    formData.append("file", file);

    axios
      .post("http://localhost:5000/api/upload", formData)
      .then((response) => {
        setCsvUrl(response.data.csv_file);
        setHtmlUrl(response.data.html_file);
      })
      .catch((error) => {
        setError(error);
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>File Upload and Download</h1>
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleFileUpload}>Upload</button>
        {csvUrl && (
          <div>
            <h3>Download CSV File</h3>
            <a
              href={`http://localhost:5000${csvUrl}`}
              download="stock_ranking.csv"
            >
              Download CSV File
            </a>
          </div>
        )}
        {htmlUrl && (
          <div>
            <h3>Download HTML File</h3>
            <a
              href={`http://localhost:5000${htmlUrl}`}
              download="stock_ranking.html"
            >
              Download HTML File
            </a>
          </div>
        )}
        {error && <div>Error: {error.message}</div>}
      </header>
    </div>
  );
}

export default App;

/* import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [downloadUrl, setDownloadUrl] = useState("");
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleFileUpload = () => {
    const formData = new FormData();
    formData.append("file", file);

    axios
      .post("http://localhost:5000/api/upload", formData, {
        responseType: "blob", // Important for downloading file
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((response) => {
        const url = window.URL.createObjectURL(
          new Blob([response.data], { type: "text/html" })
        );
        setDownloadUrl(url);
      })
      .catch((error) => {
        setError(error);
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>File Upload and Download</h1>
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleFileUpload}>Upload</button>
        {downloadUrl && (
          <div>
            <h3>Download Processed File</h3>
            <a href={downloadUrl} download="processed_data.html">
              Download HTML File
            </a>
          </div>
        )}
        {error && <div>Error: {error.message}</div>}
      </header>
    </div>
  );
}

export default App; */

/* import React, { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5000/api/data")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        setData(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Data from Flask</h1>
        {data ? (
          <div>
            <p>Message: {data.message}</p>
            <p>Status: {data.status}</p>
          </div>
        ) : (
          <p>No data found</p>
        )}
      </header>
    </div>
  );
}

export default App;
 */
