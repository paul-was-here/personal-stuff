my_daq = daq("adi");
addinput(my_daq,'smu1','a','Voltage');
my_daq.ScansAvailableFnCount = my_daq.Rate;
my_daq.ScansAvailableFcn = @(src, evt) plot_data(src, evt);
start(my_daq, "continuous");

fig = figure;
set(fig, 'CloseRequestFcn', @(src, evt) stop_daq(src, evt, my_daq));

bufferSize = 5*my_daq.Rate;
dataBuffer = zeros(bufferSize, 1);
timeBuffer = zeros(bufferSize, 1);


function plot_data(src, ~)
    persistent dataBuffer timeBuffer
    
    if isempty(dataBuffer)
        bufferSize = 5 * src.Rate;
        dataBuffer = zeros(bufferSize, 1);
        timeBuffer = zeros(bufferSize, 1);
    end

    [data, ts] = read(src, src.ScansAvailableFnCount, "OutputFormat", "Matrix");

    % Update Buffers
    dataBuffer = [dataBuffer(length(dataBuffer+1):end); data];
    timeBuffer = [timeBuffer(length(ts)+1:end); ts];

    % Apply bandpass filter
    fs = src.Rate;
    [b,a] = butter(2, [10 450] / (fs / 2), 'bandpass');
    filteredData = filtfilt(b, a, dataBuffer);
    
    % Rectify filtered signal
    rectifiedData = abs(filteredData);

    % Detect peaks
    [peaks, locs] = findpeaks(rectifiedData, 'MinPeakHeight', 0.1);

    % Smooth the signal using a moving avg filter
    windowSize = round(fs * 0.1); % 100ms filter
    smoothedData = movmean(rectifiedData, windowSize);

    plot(timeBuffer - timeBuffer(1), dataBuffer, 'b');
    hold on;
    plot(timeBuffer - timeBuffer(1), filteredData, 'r');
    plot(timeBuffer - timeBuffer(1), rectifiedData, 'g');
    plot(timeBuffer - timeBuffer(1), smoothedData, 'm');
    hold off;
    ylabel("Voltage (V)");
    xlabel("Time (s)");
    legend('Raw Data','Filtered Data','Rectified Data','SmoothedData');
    xlim([0 5]);
end

function stop_daq(~, ~, daq0bj)
    stop(daq0bk);
    delete(gcf);
end