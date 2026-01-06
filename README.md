# SofiAIPM-AccountPayables
Sofi AI Portfolio manager project. The given code gives account payables/ trade payables data of a company for a given year.

# Company Account Payables Fetcher

A Python utility to fetch and retrieve financial data (specifically Account Payables) for companies listed on NSE (National Stock Exchange) and BSE (Bombay Stock Exchange) from a financial API.

## Overview

This tool allows you to query company financial information by providing a company ticker and fiscal year. It retrieves Account Payables data from the API and displays it in a formatted, easy-to-read manner. 

## Features

- 🔍 **Easy to Use**: Simple command-line interface for inputting company ticker and year
- 📊 **Structured Data**: Returns organized financial information
- ⚠️ **Error Handling**:  Comprehensive error handling for network issues, invalid inputs, and API errors
- ✅ **Data Validation**:  Validates ticker, year, and API key before making requests
- 🎨 **Formatted Output**: Displays results in a clean, readable format

## Prerequisites

- Python 3.6 or higher
- `requests` library

## Installation

1. **Install Python 3.6+** (if not already installed)

2. **Install the required dependency:**
   ```bash
   pip install requests
