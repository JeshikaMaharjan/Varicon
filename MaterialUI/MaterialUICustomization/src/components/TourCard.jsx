import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import niagra from "../assets/images/niagra.jpg";
import Typography from "@mui/material/Typography";
import { AccessTime } from "@mui/icons-material";
import Rating from "@mui/material/Rating";
import { createTheme, ThemeProvider } from "@mui/material";

const Theme = createTheme({
  components: {
    MuiTypography: {
      variants: [
        {
          props: {
            variant: "body2",
          },
          style: {
            fontSize: 11,
            // background: "red",
          },
        },
      ],
    },
  },
});

const TourCard = ({ tour }) => {
  return (
    <Grid item xs={3}>
      <ThemeProvider theme={Theme}>
        <Paper elevation={3}>
          <img src={tour.image} className="img" />
          <Box paddingX={1}>
            <Typography variant="subtitle2" component="h4">
              {tour.name}
            </Typography>
            <Box sx={{ display: "flex", alignItems: "center" }}>
              <AccessTime sx={{ width: 12.5 }} />
              <Typography variant="body2" component="p" marginLeft={0.5}>
                {tour.duration}
              </Typography>
            </Box>
            <Box
              sx={{ display: "flex", alignItems: "center", flexWrap: "wrap" }}
            >
              <Rating
                name="read-only"
                value={tour.rating}
                readOnly
                precision={0.5}
              />
              <Typography variant="body2">{tour.rating}</Typography>
            </Box>
            <Box>
              <Typography variant="h6">(From C {tour.price})</Typography>
            </Box>
          </Box>
        </Paper>
      </ThemeProvider>
    </Grid>
  );
};
export default TourCard;
