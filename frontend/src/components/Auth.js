import React, { useState } from "react";
import axios from "axios";
import {
  Container,
  Paper,
  Typography,
  Button,
  TextField,
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
  message: {
    marginTop: theme.spacing(2),
    fontSize: "1rem",
    color: "#ff0000",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
}));

const Auth = ({ setToken, setIsAuthenticated }) => {
  const classes = useStyles();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [isLogin, setIsLogin] = useState(true);

  const handleAuth = (endpoint) => {
    axios
      .post(`http://localhost:5000/auth/${endpoint}`, {
        username,
        password,
      })
      .then((response) => {
        if (endpoint === "login") {
          setToken(response.data.access_token);
          setIsAuthenticated(true);
        } else {
          setMessage("User registered successfully");
        }
      })
      .catch((error) => {
        setMessage("Error during authentication");
      });
  };

  return (
    <Container maxWidth="sm">
      <Paper className={classes.root}>
        <Typography variant="h4" gutterBottom>
          {isLogin ? "Login" : "Register"}
        </Typography>
        <div className={classes.form}>
          <TextField
            label="Username"
            type="text"
            fullWidth
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <TextField
            label="Password"
            type="password"
            fullWidth
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            style={{ marginTop: "16px" }}
          />
          <Button
            variant="contained"
            color="primary"
            onClick={() => handleAuth(isLogin ? "login" : "register")}
            style={{ marginTop: "16px" }}
          >
            {isLogin ? "Login" : "Register"}
          </Button>
          <Button
            variant="text"
            color="primary"
            onClick={() => setIsLogin(!isLogin)}
            style={{ marginTop: "16px" }}
          >
            {isLogin ? "Need an account? Register" : "Have an account? Login"}
          </Button>
          {message && (
            <Typography className={classes.message}>{message}</Typography>
          )}
        </div>
      </Paper>
    </Container>
  );
};

export default Auth;
