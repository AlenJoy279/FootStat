package com.example.footstattest.util;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.lifecycle.LiveData;
import androidx.recyclerview.widget.RecyclerView;

import com.example.footstattest.R;
import com.example.footstattest.models.ConvertedWinner;

import java.util.List;
import java.util.Objects;

// An adapter like the listview adapter but recycler views feature extra functionality such as
// updatable contents, database support and list item resource management
public class RecyclerViewAdapter extends RecyclerView.Adapter<RecyclerViewAdapter.ViewHolder>{

    private List<ConvertedWinner> winnerList;
    private Context context;

    public RecyclerViewAdapter(List<ConvertedWinner> winnerList, Context context) {
        this.winnerList = winnerList;
        this.context = context;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {

        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.winner_row,
                parent, false);
        
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        ConvertedWinner winner = Objects.requireNonNull(winnerList.get(position));

        holder.league_name.setText(winner.getLeagueName());
        holder.winner_name.setText(winner.getShortName());
        holder.year.setText(winner.getSeasonEndDate().substring(0, 4));
        holder.crest.setImageDrawable(winner.getCrest());



    }

    @Override
    public int getItemCount() {
        return winnerList.size();
    }

    public class ViewHolder extends RecyclerView.ViewHolder {

        public TextView league_name;
        public TextView winner_name;
        public TextView year;
        public ImageView crest;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            
            league_name = itemView.findViewById(R.id.textRowL);
            winner_name = itemView.findViewById(R.id.textRowWin);
            year = itemView.findViewById(R.id.textRowYear);
            crest = itemView.findViewById(R.id.imageView);

        }
    }

}
