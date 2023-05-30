<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Symfony\Component\Process\Exception\ProcessFailedException;
use Symfony\Component\Process\Process;
use App\Models\YourModel; // Replace with your actual model

class ImageController extends Controller
{
    public function storeAndProcessImage(Request $request)
    {
        // Validate and store the image
        $request->validate([
            'image' => 'required|image|mimes:jpeg,png,jpg,gif|max:2048',
        ]);

        $imagePath = $request->file('image')->store('images');

        // Create a new process to execute the Python file
        $process = new Process(['python', 'app/Python/modelinfo.py', $imagePath]);

        try {
            // Run the process
            $process->mustRun();

            // Get the output from the process
            $output = $process->getOutput();

            // Perform a database search based on the output value
            $result = YourModel::where('number', $output)->get();

            // Return the search result as a response
            return response()->json(['result' => $result]);
        } catch (ProcessFailedException $exception) {
            // Handle any errors that occurred during the process execution
            return response()->json(['error' => $exception->getMessage()], 500);
        }
    }
}
