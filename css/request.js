const urls = {
  "lcm-iot-netilion": "https://github.com/PCPS/lcm-iot-netilion/branches/yours",
  "lcm-iot-health": "https://github.com/PCPS/lcm-iot-health/branches/yours",
  "lcm-iot-inventory":
    "https://github.com/PCPS/lcm-iot-inventory/branches/yours",
  "lcm-iot-library": "https://github.com/PCPS/lcm-iot-library/branches/yours",
  "lcm-iot-value": "https://github.com/PCPS/lcm-iot-value/branches/yours",
  "lcm-iot-bc1": "https://github.com/PCPS/lcm-iot-bc1/branches/yours",
  "lcm-iot-id": "https://github.com/PCPS/lcm-iot-id/branches/yours",
  "lcm-iot-commons": "https://github.com/PCPS/lcm-iot-commons/branches/yours",
  "lcm-information-hub-1":
    "https://github.com/PCPS/lcm-information-hub-1/branches/yours",
  "lcm-iot-fermentation":
    "https://github.com/PCPS/iot-fermentation/branches/yours",
  "lcm-iot-floodlight":
    "https://github.com/PCPS/lcm-iot-floodlight/branches/yours",
  "lcm-iot-fum": "https://github.com/PCPS/lcm-iot-fum/branches/yours",
  "lcm-iot-fus": "https://github.com/PCPS/lcm-iot-fus/branches/yours",
  "lcm-iot-wqmp": "https://github.com/PCPS/lcm-iot-floodlight/branches/yours",
};


const fetchData = async () => {
  try {
    const requests = Object.entries(urls).map(([key, url]) =>
      fetch(url)
        .then((response) => ({
          key,
          url,
          response,
        }))
        .catch((error) => ({ key, url, error }))
    );

    const responses = await Promise.allSettled(requests);

    const dataPromises = responses
      .filter((result) => result.status === "fulfilled")
      .map((result) => result.value)
      .filter(({ response }) => response.ok)
      .map(({ response, key, url }) =>
        response.json().then((data) => ({
          key,
          url,
          data,
        }))
      );

    const dataList = await Promise.allSettled(dataPromises);

    dataList
      .filter((result) => result.status === "fulfilled")
      .map((result) => result.value)
      .forEach(({ key, url, data }) => {
        const branches = data.payload.branches;
        console.log(key);
        branches.forEach((branch) => {
          console.log(branch.name);
        });
        console.log("\n");
      });
  } catch (error) {
    console.error("Error Occurs");
  }
};

fetchData();
