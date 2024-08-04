import React, { useState } from "react";
import axios from "axios";
import {
  Container,
  Paper,
  Typography,
  Button,
  CircularProgress,
  TextField,
  Grid,
  makeStyles,
} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  root: {
    padding: theme.spacing(4),
    marginTop: theme.spacing(8),
  },
  input: {
    display: "none",
  },
  button: {
    margin: theme.spacing(2, 0),
  },
  maInputs: {
    margin: theme.spacing(2, 0),
  },
  results: {
    marginTop: theme.spacing(2),
  },
  message: {
    marginTop: theme.spacing(2),
    fontSize: "1rem",
    color: "#ff0000",
  },
}));

const FileUpload = ({ token }) => {
  const classes = useStyles();
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const [csvUrl, setCsvUrl] = useState(null);
  const [htmlUrl, setHtmlUrl] = useState(null);
  const [maPeriod1, setMaPeriod1] = useState(9);
  const [maPeriod2, setMaPeriod2] = useState(21);

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
    formData.append("ma_period1", maPeriod1);
    formData.append("ma_period2", maPeriod2);

    try {
      setLoading(true);
      setMessage("Uploading...");
      const res = await axios.post(
        "http://localhost:5000/api/upload",
        formData,
        {
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "multipart/form-data",
          },
        }
      );
      setMessage(res.data.message);
      setCsvUrl(res.data.csv_file);
      setHtmlUrl(res.data.html_file);
    } catch (err) {
      console.error(err);
      setMessage(
        "Error uploading file: " +
          (err.response ? err.response.data.message : err.message)
      );
    } finally {
      setLoading(false);
    }
  };

  const handleDownload = (url, filename) => {
    axios
      .get(url, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
        responseType: "blob",
      })
      .then((response) => {
        const downloadUrl = window.URL.createObjectURL(
          new Blob([response.data])
        );
        const link = document.createElement("a");
        link.href = downloadUrl;
        link.setAttribute("download", filename);
        document.body.appendChild(link);
        link.click();
        link.remove(); // Clean up the DOM after download
      })
      .catch((error) => {
        setMessage(
          "Error downloading file: " +
            (error.response ? error.response.data.message : error.message)
        );
      });
  };

  return (
    <Container maxWidth="sm">
      <Paper className={classes.root}>
        <Typography variant="h5" gutterBottom>
          File Upload
        </Typography>
        <form onSubmit={handleFileUpload}>
          <input
            accept=".csv"
            className={classes.input}
            id="file-upload"
            type="file"
            onChange={handleFileChange}
          />
          <label htmlFor="file-upload">
            <Button variant="contained" color="primary" component="span">
              Choose File
            </Button>
          </label>
          <Grid container spacing={2} className={classes.maInputs}>
            <Grid item xs={6}>
              <TextField
                label="MA Fast"
                type="number"
                fullWidth
                value={maPeriod1}
                onChange={(e) => setMaPeriod1(e.target.value)}
              />
            </Grid>
            <Grid item xs={6}>
              <TextField
                label="MA Slow"
                type="number"
                fullWidth
                value={maPeriod2}
                onChange={(e) => setMaPeriod2(e.target.value)}
              />
            </Grid>
          </Grid>
          <Button
            variant="contained"
            color="secondary"
            className={classes.button}
            type="submit"
            disabled={loading}
          >
            {loading ? <CircularProgress size={24} /> : "Upload"}
          </Button>
        </form>
        {message && (
          <Typography className={classes.message}>{message}</Typography>
        )}
        <div className={classes.results}>
          {csvUrl && (
            <Button
              variant="contained"
              color="default"
              onClick={() =>
                handleDownload(
                  `http://localhost:5000${csvUrl}`,
                  "stock_ranking.csv"
                )
              }
            >
              Download CSV File
            </Button>
          )}
          {htmlUrl && (
            <Button
              variant="contained"
              color="default"
              onClick={() =>
                handleDownload(
                  `http://localhost:5000${htmlUrl}`,
                  "stock_ranking.html"
                )
              }
            >
              Download HTML File
            </Button>
          )}
        </div>
      </Paper>
    </Container>
  );
};

export default FileUpload;

// import React, { useState } from "react";
// import axios from "axios";
// import {
//   Container,
//   Paper,
//   Typography,
//   Button,
//   CircularProgress,
//   TextField,
//   Grid,
//   makeStyles,
// } from "@material-ui/core";

// const useStyles = makeStyles((theme) => ({
//   root: {
//     padding: theme.spacing(4),
//     marginTop: theme.spacing(8),
//   },
//   input: {
//     display: "none",
//   },
//   button: {
//     margin: theme.spacing(2, 0),
//   },
//   maInputs: {
//     margin: theme.spacing(2, 0),
//   },
//   results: {
//     marginTop: theme.spacing(2),
//   },
//   message: {
//     marginTop: theme.spacing(2),
//     fontSize: "1rem",
//     color: "#ff0000",
//   },
// }));

// const FileUpload = ({ token }) => {
//   const classes = useStyles();
//   const [file, setFile] = useState(null);
//   const [message, setMessage] = useState("");
//   const [loading, setLoading] = useState(false);
//   const [csvUrl, setCsvUrl] = useState(null);
//   const [htmlUrl, setHtmlUrl] = useState(null);
//   const [maPeriod1, setMaPeriod1] = useState(9);
//   const [maPeriod2, setMaPeriod2] = useState(21);

//   const handleFileChange = (e) => {
//     setFile(e.target.files[0]);
//   };

//   const handleFileUpload = async (e) => {
//     e.preventDefault();
//     if (!file) {
//       setMessage("Please select a file to upload");
//       return;
//     }

//     const formData = new FormData();
//     formData.append("file", file);
//     formData.append("ma_period1", maPeriod1);
//     formData.append("ma_period2", maPeriod2);

//     try {
//       setLoading(true);
//       setMessage("Uploading...");
//       const res = await axios.post(
//         "http://localhost:5000/api/upload",
//         formData,
//         {
//           headers: {
//             Authorization: `Bearer ${token}`,
//             "Content-Type": "multipart/form-data",
//           },
//         }
//       );
//       setMessage(res.data.message);
//       setCsvUrl(res.data.csv_file);
//       setHtmlUrl(res.data.html_file);
//     } catch (err) {
//       console.error(err);
//       setMessage(
//         "Error uploading file: " +
//           (err.response ? err.response.data.message : err.message)
//       );
//     } finally {
//       setLoading(false);
//     }
//   };

//   const handleDownload = (url, filename) => {
//     axios
//       .get(url, {
//         headers: {
//           Authorization: `Bearer ${token}`,
//         },
//         responseType: "blob",
//       })
//       .then((response) => {
//         const downloadUrl = window.URL.createObjectURL(
//           new Blob([response.data])
//         );
//         const link = document.createElement("a");
//         link.href = downloadUrl;
//         link.setAttribute("download", filename);
//         document.body.appendChild(link);
//         link.click();
//         link.remove(); // Clean up the DOM after download
//       })
//       .catch((error) => {
//         setMessage(
//           "Error downloading file: " +
//             (error.response ? error.response.data.message : error.message)
//         );
//       });
//   };

//   return (
//     <div className="file-upload">
//       <form onSubmit={handleFileUpload}>
//         <input
//           accept=".csv"
//           className={classes.input}
//           id="file-upload"
//           type="file"
//           onChange={handleFileChange}
//         />
//         <label htmlFor="file-upload">
//           <Button variant="contained" color="primary" component="span">
//             Choose File
//           </Button>
//         </label>
//         <Grid container spacing={2} className={classes.maInputs}>
//           <Grid item xs={6}>
//             <TextField
//               label="MA Fast"
//               type="number"
//               fullWidth
//               value={maPeriod1}
//               onChange={(e) => setMaPeriod1(e.target.value)}
//             />
//           </Grid>
//           <Grid item xs={6}>
//             <TextField
//               label="MA Slow"
//               type="number"
//               fullWidth
//               value={maPeriod2}
//               onChange={(e) => setMaPeriod2(e.target.value)}
//             />
//           </Grid>
//         </Grid>
//         <Button
//           variant="contained"
//           color="secondary"
//           className={classes.button}
//           type="submit"
//           disabled={loading}
//         >
//           {loading ? <CircularProgress size={24} /> : "Upload"}
//         </Button>
//       </form>
//       {message && (
//         <Typography className={classes.message}>{message}</Typography>
//       )}
//       <div className={classes.results}>
//         {csvUrl && (
//           <Button
//             variant="contained"
//             color="default"
//             onClick={() =>
//               handleDownload(
//                 `http://localhost:5000${csvUrl}`,
//                 "stock_ranking.csv"
//               )
//             }
//           >
//             Download CSV File
//           </Button>
//         )}
//         {htmlUrl && (
//           <Button
//             variant="contained"
//             color="default"
//             onClick={() =>
//               handleDownload(
//                 `http://localhost:5000${htmlUrl}`,
//                 "stock_ranking.html"
//               )
//             }
//           >
//             Download HTML File
//           </Button>
//         )}
//       </div>
//     </div>
//   );
// };

// export default FileUpload;

// import React, { useState } from "react";
// import axios from "axios";
// // import "./FileUpload.css";

// const FileUpload = () => {
//   const [file, setFile] = useState(null);
//   const [message, setMessage] = useState("");
//   const [loading, setLoading] = useState(false);
//   const [csvUrl, setCsvUrl] = useState(null);
//   const [htmlUrl, setHtmlUrl] = useState(null);

//   const onChange = (e) => {
//     setFile(e.target.files[0]);
//   };

//   const onSubmit = async (e) => {
//     e.preventDefault();
//     if (!file) {
//       setMessage("Please select a file to upload");
//       return;
//     }

//     const formData = new FormData();
//     formData.append("file", file);

//     try {
//       setLoading(true);
//       setMessage("");
//       const res = await axios.post(
//         "http://localhost:5000/api/upload",
//         formData,
//         {
//           headers: {
//             "Content-Type": "multipart/form-data",
//           },
//         }
//       );
//       setMessage(res.data.message);
//       setCsvUrl(`http://localhost:5000${res.data.csv_file}`);
//       setHtmlUrl(`http://localhost:5000${res.data.html_file}`);
//     } catch (err) {
//       setMessage("Error uploading file");
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="file-upload">
//       <form onSubmit={onSubmit}>
//         <div className="file-upload-input">
//           <input type="file" onChange={onChange} />
//         </div>
//         <button type="submit" disabled={loading}>
//           {loading ? "Uploading..." : "Upload"}
//         </button>
//       </form>
//       {message && <p>{message}</p>}
//       {csvUrl && (
//         <div>
//           <h2>Results</h2>
//           <a href={csvUrl} download="stock_ranking.csv">
//             Download CSV Results
//           </a>
//         </div>
//       )}
//       {htmlUrl && (
//         <div>
//           <a href={htmlUrl} download="stock_ranking.html">
//             Download HTML Results
//           </a>
//         </div>
//       )}
//     </div>
//   );
// };

// export default FileUpload;
