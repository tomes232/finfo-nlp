import React from 'react'; 
import PropTypes from 'prop-types'
import LoginRegister from 'react-mui-login-register';


class LoginPage extends Component {
    constructor(props){
        
    }
    
    render() {
  
      const header = (
          <AppBar position="static">
            <Toolbar>
              <Typography variant="title" color="inherit">Welcome</Typography>
            </Toolbar>
          </AppBar>
      );
  
      const footer = (
          <div className={classes.footer}>
            <Typography variant="caption" align="center">v0.9</Typography>
          </div>
      );
  
      return (
          <div>
            <LoginRegister header={header} footer={footer}
                           onLogin={this.handleLogin}
                           onLoginWithProvider={this.handleLoginWithProvider}
                           onRegister={this.handleRegister}
                           onRegisterWithProvider={this.handleRegisterWithProvider}
            />
          </div>);
    }
  
    handleLogin = content => {
      alert(`Logging in with content '${JSON.stringify(content)}'`);
    };
  
    handleLoginWithProvider = providerId => {
      alert(`Logging in with provider '${providerId}'`);
    };
  
    handleRegister = content => {
      alert(`Registering with content '${JSON.stringify(content)}'`);
    };
  
    handleRegisterWithProvider = providerId => {
      alert(`Registering with provider '${providerId}'`);
    };
  }

export default LoginPage; 
