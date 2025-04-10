# Monte Carlo Method in Fintech Data Processing

This project implements a Monte Carlo simulation for startup valuation and prediction using Streamlit. The application provides a user-friendly interface to run parallelized Monte Carlo simulations and visualize the results.

## Features

- Parallel computing implementation using Numba for efficient Monte Carlo simulations
- Interactive Streamlit interface for parameter adjustment
- Real-time visualization of simulation results
- Statistical analysis of valuation outcomes
- Distribution analysis of final valuations

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Adjust the simulation parameters in the sidebar:
   - Initial Valuation
   - Expected Growth Rate
   - Volatility
   - Time Horizon
   - Number of Simulations

3. Click "Run Simulation" to start the Monte Carlo simulation

4. View the results:
   - Simulation paths visualization
   - Statistical metrics (mean, median, standard deviation)
   - Distribution of final valuations

## Technical Details

The Monte Carlo simulation uses Geometric Brownian Motion to model the startup's valuation over time. The implementation leverages:

- Numba for parallel computing
- NumPy for efficient numerical computations
- Plotly for interactive visualizations
- Streamlit for the web interface

## License

This project is licensed under the MIT License - see the LICENSE file for details.