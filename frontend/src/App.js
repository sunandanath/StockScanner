import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import Auth from "./components/Auth";
import { Container, Paper, Typography, makeStyles } from "@material-ui/core";
import "./App.css";

const useStyles = makeStyles((theme) => ({
  root: {
    padding: theme.spacing(4),
    marginTop: theme.spacing(8),
  },
}));

function App() {
  const classes = useStyles();
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [token, setToken] = useState("");

  if (!isAuthenticated) {
    return <Auth setToken={setToken} setIsAuthenticated={setIsAuthenticated} />;
  }

  return (
    <Container maxWidth="sm">
      <Paper className={classes.root}>
        <Typography variant="h4" gutterBottom>
          Stock Analyzer
        </Typography>
        <Typography variant="h6" gutterBottom>
          Support and Resistance Strategy
        </Typography>
        <FileUpload token={token} />
      </Paper>
    </Container>
  );
}

export default App;

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
// import "./App.css";

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
//   loginForm: {
//     display: "flex",
//     flexDirection: "column",
//     alignItems: "center",
//   },
// }));

// function App() {
//   const classes = useStyles();
//   const [file, setFile] = useState(null);
//   const [csvUrl, setCsvUrl] = useState("");
//   const [htmlUrl, setHtmlUrl] = useState("");
//   const [message, setMessage] = useState("");
//   const [loading, setLoading] = useState(false);
//   const [maPeriod1, setMaPeriod1] = useState(9);
//   const [maPeriod2, setMaPeriod2] = useState(21);
//   const [username, setUsername] = useState("");
//   const [password, setPassword] = useState("");
//   const [isAuthenticated, setIsAuthenticated] = useState(false);
//   const [token, setToken] = useState("");

//   const handleFileChange = (e) => {
//     setFile(e.target.files[0]);
//   };

//   const handleFileUpload = (e) => {
//     e.preventDefault();
//     if (!file) {
//       setMessage("Please select a file to upload");
//       return;
//     }

//     const formData = new FormData();
//     formData.append("file", file);
//     formData.append("ma_period1", maPeriod1);
//     formData.append("ma_period2", maPeriod2);

//     setLoading(true);
//     setMessage("Uploading...");
//     setTimeout(() => {
//       setMessage("Data Processing");
//       axios
//         .post("http://localhost:5000/api/upload", formData, {
//           headers: {
//             Authorization: `Bearer ${token}`,
//             "Content-Type": "multipart/form-data",
//           },
//         })
//         .then((response) => {
//           setCsvUrl(`http://localhost:5000${response.data.csv_file}`);
//           setHtmlUrl(`http://localhost:5000${response.data.html_file}`);
//           setMessage(response.data.message);
//         })
//         .catch((error) => {
//           setMessage("Error uploading file");
//         })
//         .finally(() => {
//           setLoading(false);
//         });
//     }, 500); // Delay to show "Data Processing"
//   };

//   const handleLogin = () => {
//     axios
//       .post("http://localhost:5000/login", {
//         username,
//         password,
//       })
//       .then((response) => {
//         setToken(response.data.access_token);
//         setIsAuthenticated(true);
//       })
//       .catch((error) => {
//         setMessage("Invalid credentials");
//       });
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
//         const url = window.URL.createObjectURL(new Blob([response.data]));
//         const link = document.createElement("a");
//         link.href = url;
//         link.setAttribute("download", filename);
//         document.body.appendChild(link);
//         link.click();
//       })
//       .catch((error) => {
//         setMessage("Error downloading file");
//       });
//   };

//   if (!isAuthenticated) {
//     return (
//       <Container maxWidth="sm">
//         <Paper className={classes.root}>
//           <Typography variant="h4" gutterBottom>
//             Login
//           </Typography>
//           <div className={classes.loginForm}>
//             <TextField
//               label="Username"
//               type="text"
//               fullWidth
//               value={username}
//               onChange={(e) => setUsername(e.target.value)}
//             />
//             <TextField
//               label="Password"
//               type="password"
//               fullWidth
//               value={password}
//               onChange={(e) => setPassword(e.target.value)}
//               style={{ marginTop: "16px" }}
//             />
//             <Button
//               variant="contained"
//               color="primary"
//               onClick={handleLogin}
//               style={{ marginTop: "16px" }}
//             >
//               Login
//             </Button>
//             {message && (
//               <Typography className={classes.message}>{message}</Typography>
//             )}
//           </div>
//         </Paper>
//       </Container>
//     );
//   }

//   return (
//     <Container maxWidth="sm">
//       <Paper className={classes.root}>
//         <Typography variant="h4" gutterBottom>
//           Stock Analyzer
//         </Typography>
//         <Typography variant="h6" gutterBottom>
//           Support and Resistance Strategy
//         </Typography>
//         <form onSubmit={handleFileUpload}>
//           <input
//             accept=".csv"
//             className={classes.input}
//             id="file-upload"
//             type="file"
//             onChange={handleFileChange}
//           />
//           <label htmlFor="file-upload">
//             <Button variant="contained" color="primary" component="span">
//               Choose File
//             </Button>
//           </label>
//           <Grid container spacing={2} className={classes.maInputs}>
//             <Grid item xs={6}>
//               <TextField
//                 label="MA Fast"
//                 type="number"
//                 fullWidth
//                 value={maPeriod1}
//                 onChange={(e) => setMaPeriod1(e.target.value)}
//               />
//             </Grid>
//             <Grid item xs={6}>
//               <TextField
//                 label="MA Slow"
//                 type="number"
//                 fullWidth
//                 value={maPeriod2}
//                 onChange={(e) => setMaPeriod2(e.target.value)}
//               />
//             </Grid>
//           </Grid>
//           <Button
//             variant="contained"
//             color="secondary"
//             className={classes.button}
//             type="submit"
//             disabled={loading}
//           >
//             {loading ? <CircularProgress size={24} /> : "Upload"}
//           </Button>
//         </form>
//         {message && (
//           <Typography className={classes.message}>{message}</Typography>
//         )}
//         <div className={classes.results}>
//           {csvUrl && (
//             <Button
//               variant="contained"
//               color="default"
//               onClick={() => handleDownload(csvUrl, "stock_ranking.csv")}
//             >
//               Download CSV File
//             </Button>
//           )}
//           {htmlUrl && (
//             <Button
//               variant="contained"
//               color="default"
//               onClick={() => handleDownload(htmlUrl, "stock_ranking.html")}
//             >
//               Download HTML File
//             </Button>
//           )}
//         </div>
//       </Paper>
//     </Container>
//   );
// }

// export default App;
