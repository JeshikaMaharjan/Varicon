import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import niagra from "../assets/images/niagra.jpg";
import Typography from "@mui/material/Typography";
import { AccessTime } from "@mui/icons-material";
import Rating from "@mui/material/Rating";
import { useState } from "react";

const TourCard = () => {
  const [value, setValue] = useState(2.5);

  return (
    <Grid item xs={3}>
      <Paper elevation={3}>
        <img src={niagra} className="img" />
        <Box paddingX={1}>
          <Typography variant="subtitle2" component="h4">
            Immerse into the waterfall
          </Typography>
          <Box sx={{ display: "flex", alignItems: "center" }}>
            <AccessTime sx={{ width: 12.5 }} />
            <Typography variant="body2" component="p" marginLeft={0.5}>
              5 hours
            </Typography>
          </Box>
          <Box sx={{ display: "flex", alignItems: "center" }}>
            <Rating name="read-only" value={value} readOnly precision={0.5} />
            <Typography variant="body2">4.5</Typography>
          </Box>
          <Box>
            <Typography variant="h6">(From C $455)</Typography>
          </Box>
        </Box>
      </Paper>
    </Grid>
  );
};
export default TourCard;
