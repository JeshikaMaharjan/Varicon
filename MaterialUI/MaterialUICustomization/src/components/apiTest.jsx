import React from "react";
import { useQuery, useQueryClient } from "@tanstack/react-query";
import axios from "axios";

const DisplayPosts = () => {
  async function retrievePosts() {
    const response = await axios.get(
      "https://jsonplaceholder.typicode.com/posts"
    );
    console.log(response.data);
    return response.data;
  }

  const { data, isLoading, error } = useQuery({
    queryKey: ["postsData"],
    queryFn: retrievePosts,
  });

  if (isLoading) return <div>Fetching posts...</div>;
  if (error) return <div>An error occurred: {error.message}</div>;

  const newPostmutation = useMutation({
    mutationFn: (newTodo) => {
      return axios.post("/todos", newTodo);
    },
  });

  return (
    <ul>
      {data?.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
};

export default DisplayPosts;
