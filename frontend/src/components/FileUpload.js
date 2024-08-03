import React, { useState } from "react";
import axios from "axios";
import "./App.css";

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const [csvUrl, setCsvUrl] = useState(null);
  const [htmlUrl, setHtmlUrl] = useState(null);
  const [tooltipVisible, setTooltipVisible] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleFileUpload = async (e) => {
    e.preventDefault();
    if (!file) {
      setMessage("Please select a file to upload");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      setMessage("Uploading...");
      setTimeout(() => {
        setMessage("Data Processing");
        axios
          .post("http://localhost:5000/api/upload", formData, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          })
          .then((res) => {
            setCsvUrl(res.data.csv_file);
            setHtmlUrl(res.data.html_file);
            setMessage(res.data.message);
          })
          .catch((err) => {
            setMessage("Error uploading file");
          })
          .finally(() => {
            setLoading(false);
          });
      }, 500); // Delay to show "Data Processing"
    } catch (err) {
      setMessage("Error uploading file");
      setLoading(false);
    }
  };

  return (
    <div className="file-upload">
      <form onSubmit={handleFileUpload}>
        <label
          htmlFor="file-upload"
          className="file-upload-label"
          onMouseEnter={() => setTooltipVisible(true)}
          onMouseLeave={() => setTooltipVisible(false)}
        >
          Choose File
          {tooltipVisible && (
            <span className="tooltip">Choose a CSV file including Symbols</span>
          )}
        </label>
        <input
          type="file"
          id="file-upload"
          className="file-upload-input"
          onChange={handleFileChange}
        />
        <button type="submit" disabled={loading}>
          {loading ? message : "Upload"}
        </button>
      </form>
      {message && <p className="message">{message}</p>}
      <div className="results">
        {csvUrl && (
          <div>
            <h2>Results</h2>
            <a
              href={`http://localhost:5000${csvUrl}`}
              download="stock_ranking.csv"
            >
              Download CSV Results
            </a>
          </div>
        )}
        {htmlUrl && (
          <div>
            <a
              href={`http://localhost:5000${htmlUrl}`}
              download="stock_ranking.html"
            >
              Download HTML Results
            </a>
          </div>
        )}
      </div>
    </div>
  );
};

export default FileUpload;
