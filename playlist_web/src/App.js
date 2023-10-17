import axios from 'axios';
import React from 'react';
// import logo from './logo.svg';
import './App.css';



const handleLinkClick = async () => {
  try {
    const response = await fetch('http://localhost:5000', {
      method: 'GET',

    });
  } catch (error) {
    console.error('Error', error);
  }
};

function App() {

  const handleLogin = () => {
    const spotifyAuthUrl = (
        "https://accounts.spotify.com/authorize"
        + "?client_id=523af5a59f764c14971ce95056ea5ea6"
        + "&response_type=code"
        + "&redirect_uri=http://127.0.0.1:5000/playlist"
        + "&scope=playlist-modify-public user-top-read user-library-read"
    );
    window.location.href = spotifyAuthUrl;
};


  return (

    
    <div className="App">
      <header className="App-header">

      <div>
      <button onClick={handleLogin}> Login with Spotify </button>
    </div>

      <svg
              className="App-logo"
              x="0px"
              y="0px"
              viewBox="10 70 350 350"
              width="175px"
              height="175px"
            >
              <path
                d="M253.084,7.255c14.601,14.299,22.646,33.409,41.014,44.169
                c14.282,8.366,35.335,8.5,44.169,22.084c5.939,9.133,7.419,27.392,0,35.756c-5.068-35.817-35.035-32.236-57.841-49.428
                c-5.958-6.66-11.919-13.321-17.878-19.981c4.557,41.711,9.115,83.435,13.671,125.146c2.243,12.553,8.561,32.938,4.207,46.273
                c-4.949,15.16-21.632,26.625-37.859,30.498c-30.948,7.385-66.418-20.607-55.737-51.531c11.528-33.374,57.613-34.349,83.08-14.723
                C264.303,119.437,258.693,63.337,253.084,7.255z M91.131,16.72c18.335,0.109,23.3,7.739,29.446,19.981
                c24.146,48.092-3.925,92.918-25.239,125.146c3.855,16.124,7.712,32.252,11.568,48.376c83.31-2.216,86.255,108.859,28.394,127.249
                c20.391,66.648-69.765,92.072-88.338,46.272c0.701-3.504,1.402-7.011,2.104-10.516c6.455-4.587,11.014-5.638,19.981-3.155
                c3.118,4.554,4.93,6.783,5.258,14.724c-3.031,5.075-6.147,5.788-2.103,9.464c34.421,22.119,59.37-18.465,51.531-51.53
                C53.013,354.385-7.3,304.607,16.464,229.152c12.56-39.879,41.575-60.509,63.099-90.441C69.406,100.691,53.458,37.627,91.131,16.72z
                 M94.286,27.236c-27.187,17.962-17.569,72.817-9.465,105.165c0.351-0.701,0.702-1.402,1.052-2.104
                c15.737-12.747,50.499-82.22,15.774-100.958C99.194,28.639,96.739,27.938,94.286,27.236z M86.925,171.312
                c-17.209,23.01-38.111,44.916-47.324,75.719c-12.567,42.011,11.587,79.395,41.014,87.287c14.073,3.774,29.021-1.189,41.014-3.155
                c0-1.402,0-2.804,0-4.207c-7.36-35.051-14.724-70.113-22.084-105.165c-24.299,5.054-45.932,43.274-32.601,74.667
                c5.608,7.711,11.218,15.425,16.826,23.136c-1.402,0-2.805,0-4.206,0c-31.384-15.551-30.442-66.646-9.465-92.544
                c6.799-8.395,18.998-9.923,27.343-16.826C94.635,200.104,93.974,177.967,86.925,171.312z M109.009,219.688
                c8.412,34.701,16.827,69.412,25.239,104.113C172.229,297.401,164.674,221.407,109.009,219.688z M331.958,276.477
                c-0.188,25.195-21.731,102.605-35.756,112.526c-8.288,5.863-32.662,13.989-43.118,4.206c-3.886-2.521-4.219-3.958-4.207-10.516
                c6.199-14.664,30.017-25.876,49.428-16.827c3.337-18.992,16.644-43.981,12.62-62.047c-0.351,0-0.702,0-1.052,0
                c-7.049,0.944-63.298,9.471-64.15,10.517c-13.705,27.973-22.646,121.783-77.821,84.132c0-3.505,0-7.011,0-10.517
                c8.457-12.669,24.219-19.98,45.22-16.826c1.588-11.785,18.99-73.682,25.24-77.822c11.615-5.578,29.193,0.255,43.118-2.103
                C301.044,287.886,312.064,277.23,331.958,276.477z M316.183,286.993c-15.666,10.852-43.111,10.694-66.253,13.671
                c-0.351,1.402-0.701,2.805-1.052,4.207c0.701,0,1.402,0,2.104,0c17.538,7.495,54.068-5.281,65.202-11.568
                C316.183,291.2,316.183,289.096,316.183,286.993z"
                fill="black"
                stroke="black"
              ></path>
            </svg>

        <p>
          click below for a custom playlist!
        </p>
        <a
          className="App-link"
          href="http://localhost:5000/playlist" onClick={handleLinkClick}
          target="_self"
          rel="noopener noreferrer"
        >
          make me a playlist
        </a>


      </header>
    </div>
  );
}






export default App;