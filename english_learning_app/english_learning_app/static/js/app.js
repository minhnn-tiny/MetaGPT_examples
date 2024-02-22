import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Chart from 'chart.js';

function App() {
  const [flashcards, setFlashcards] = useState([]);
  const [quizzes, setQuizzes] = useState([]);
  const [userProgress, setUserProgress] = useState({ score: 0, level: '' });
  const [sessionData, setSessionData] = useState({ labels: [], scores: [] });
  const [chartInstance, setChartInstance] = useState(null);
  const [errorMessage, setErrorMessage] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const progressResponse = await axios.get('/api/progress');
        setUserProgress(progressResponse.data);

        const flashcardsResponse = await axios.get(`/api/flashcards?level=${progressResponse.data.level}`);
        setFlashcards(flashcardsResponse.data);

        const quizzesResponse = await axios.get(`/api/quizzes?level=${progressResponse.data.level}`);
        setQuizzes(quizzesResponse.data);

        const sessionResponse = await axios.get('/api/sessions');
        const sessionLabels = sessionResponse.data.map(session => session.label);
        const sessionScores = sessionResponse.data.map(session => session.score);
        setSessionData({ labels: sessionLabels, scores: sessionScores });
      } catch (error) {
        console.error('Error fetching data:', error);
        setErrorMessage('Failed to fetch data. Please try again later.');
      }
    };

    fetchData();
  }, []);

  useEffect(() => {
    if (chartInstance) {
      chartInstance.data.labels = sessionData.labels;
      chartInstance.data.datasets[0].data = sessionData.scores;
      chartInstance.update();
    } else {
      const ctx = document.getElementById('progressChart').getContext('2d');
      const newChartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: sessionData.labels,
          datasets: [{
            label: 'Score',
            data: sessionData.scores,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              }
            }]
          }
        }
      });
      setChartInstance(newChartInstance);
    }
  }, [sessionData]);

  const updateScore = async (newScore) => {
    try {
      const response = await axios.post('/api/progress', { score: newScore });
      setUserProgress(response.data);
      // Fetch updated session data to reflect the new score
      const sessionResponse = await axios.get('/api/sessions');
      const sessionLabels = sessionResponse.data.map(session => session.label);
      const sessionScores = sessionResponse.data.map(session => session.score);
      setSessionData({ labels: sessionLabels, scores: sessionScores });
    } catch (error) {
      console.error('Error updating score:', error);
      setErrorMessage('Failed to update score. Please try again later.');
    }
  };

  const handleSubmitScore = async (newScore) => {
    await updateScore(newScore);
    // Additional logic can be added here if needed
  };

  const renderFlashcards = () => flashcards.map((flashcard, index) => (
    <div key={index}>
      <p>{flashcard.content}</p>
    </div>
  ));

  const renderQuizzes = () => quizzes.map((quiz, index) => (
    <div key={index}>
      <p>{quiz.difficulty_level}</p>
      {quiz.questions && quiz.questions.map((question, qIndex) => (
        <div key={qIndex}>
          <p>{question}</p>
        </div>
      ))}
    </div>
  ));

  return (
    <div className="App">
      <h1>English Learning App</h1>
      {errorMessage && <p className="error-message">{errorMessage}</p>}
      <div>{renderFlashcards()}</div>
      <div>{renderQuizzes()}</div>
      <button onClick={() => handleSubmitScore(userProgress.score + 1)}>Update Score</button>
      <canvas id="progressChart" width="400" height="400"></canvas>
    </div>
  );
}

export default App;
