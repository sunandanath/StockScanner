import React, { useState } from "react";
import axios from "axios";
// import "./FileUpload.css";

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const [csvUrl, setCsvUrl] = useState(null);
  const [htmlUrl, setHtmlUrl] = useState(null);

  const onChange = (e) => {
    setFile(e.target.files[0]);
  };

  const onSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setMessage("Please select a file to upload");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      setMessage("");
      const res = await axios.post("/api/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setMessage(res.data.message);
      setCsvUrl(res.data.csv_file);
      setHtmlUrl(res.data.html_file);
    } catch (err) {
      setMessage("Error uploading file");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="file-upload">
      <form onSubmit={onSubmit}>
        <div className="file-upload-input">
          <input type="file" onChange={onChange} />
        </div>
        <button type="submit" disabled={loading}>
          {loading ? "Uploading..." : "Upload"}
        </button>
      </form>
      {message && <p>{message}</p>}
      {csvUrl && (
        <div>
          <h2>Results</h2>
          <a href={csvUrl} download="stock_ranking.csv">
            Download CSV Results
          </a>
        </div>
      )}
      {htmlUrl && (
        <div>
          <a href={htmlUrl} download="stock_ranking.html">
            Download HTML Results
          </a>
        </div>
      )}
    </div>
  );
};

export default FileUpload;
