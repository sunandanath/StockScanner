import React, { useState } from "react";
import axios from "axios";
import "./FileUpload.css";

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

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
      const res = await axios.post(
        "http://localhost:5000/api/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      setMessage(res.data.message);
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
          Upload
        </button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default FileUpload;
