import "./App.css";
import TourCard from "./components/TourCard";
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import SearchAppBar from "./components/AppBar";
import cities from "./data.json";
import Typography from "@mui/material/Typography";
import DisplayPosts from "./components/apiTest";

function App() {
  return (
    // <div className="App">
    //   <SearchAppBar />
    //   <Container sx={{ marginY: 5 }}>
    //     {cities.map((city) => (
    //       <>
    //         <Typography variant="h4" marginTop={5}>
    //           Top {city.name}
    //         </Typography>
    //         <Grid container spacing={5}>
    //           {city.tours.map((tour, index) => (
    //             <TourCard tour={tour} key={index} />
    //           ))}
    //         </Grid>
    //       </>
    //     ))}
    //   </Container>
    // </div>

    //......................................
    // React Query

    <DisplayPosts />
  );
}

export default App;
