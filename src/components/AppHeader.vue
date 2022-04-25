<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">United Auto Sales</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink to="/register" class="nav-link active">Register</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink to="/explore" class="nav-link active">Explore</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink to="/users" class="nav-link active">Users</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink to="/cars/new" class="nav-link active">Add Car</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink to="/about" class="nav-link active">About</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink to="/login" class="nav-link active">Login</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { RouterLink } from "vue-router";
</script>

<style>
/* Add any component specific styles here */
</style>