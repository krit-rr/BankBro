import moment from "moment";
import "moment-timezone";

export const unixToDateString = (timestamp) => {
  if (timestamp === null) return null;

  const timezone = "America/New_York";
  const date = moment(timestamp).tz(timezone).format("MMMM DD, YYYY, h:mm A z");
  return date;
};

export const getRelativeTime = (timestamp) => {
  return moment(timestamp).fromNow();
};
