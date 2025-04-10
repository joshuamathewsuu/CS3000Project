# Monte Carlo Method in Fintech Data Processing

This project implements a Monte Carlo simulation for startup valuation and prediction using Streamlit. The application provides a user-friendly interface to run parallelized Monte Carlo simulations and visualize the results.

## Features

- Parallel computing implementation using Numba for efficient Monte Carlo simulations
- Industry-specific analysis for different sectors (Technology, Healthcare, Finance, Retail, Manufacturing)
- Interactive Streamlit interface for parameter adjustment
- Real-time visualization of simulation results
- Statistical analysis of valuation outcomes
- Distribution analysis of final valuations
- Industry insights and benchmarks

## Prerequisites

- Python 3.13 or higher
- Homebrew (for macOS users)
- Git

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/joshuamathewsuu/CS3000Project.git
cd CS3000Project
```

### 2. Install System Dependencies (macOS)

```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install required system packages
brew install openblas
brew install pkg-config
brew install scipy
```

### 3. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate
```

### 4. Install Python Dependencies

```bash
# Install required Python packages
pip install -r requirements.txt

# If you encounter any issues, install packages individually:
pip install streamlit==1.32.0
pip install numpy==1.26.4
pip install pandas==2.2.1
pip install scipy==1.12.0
pip install matplotlib==3.8.3
pip install plotly==5.19.0
pip install numba==0.59.0
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Access the application in your web browser:
   - Local URL: http://localhost:8501
   - Network URL: http://[your-ip]:8501

3. Adjust the simulation parameters in the sidebar:
   - Select Industry
   - Initial Valuation
   - Expected Growth Rate
   - Volatility
   - Time Horizon
   - Number of Simulations

4. Click "Run Simulation" to start the Monte Carlo simulation

5. View the results:
   - Simulation paths visualization
   - Statistical metrics (mean, median, standard deviation)
   - Distribution of final valuations
   - Industry insights

## Technical Details

The Monte Carlo simulation uses Geometric Brownian Motion to model the startup's valuation over time. The implementation leverages:

- Numba for parallel computing
- NumPy for efficient numerical computations
- Plotly for interactive visualizations
- Streamlit for the web interface

### Industry-Specific Parameters

The application includes predefined parameters for different industries:

| Industry      | Growth Rate Range | Volatility Range |
|--------------|------------------|------------------|
| Technology   | 15% - 40%        | 25% - 50%        |
| Healthcare   | 10% - 30%        | 20% - 40%        |
| Finance      | 12% - 35%        | 22% - 45%        |
| Retail       | 8% - 25%         | 15% - 35%        |
| Manufacturing| 5% - 20%         | 10% - 30%        |

## Project Structure

```
CS3000Project/
├── .venv/                  # Virtual environment
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── LICENSE                # License file
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by various startup analysis repositories
- Uses industry-standard Monte Carlo simulation techniques
- Built with modern Python data science tools